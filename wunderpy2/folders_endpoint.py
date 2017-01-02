'''
Encapsulates all tasks that can be run against the 'folders' endpoint
'''


def _check_title_length(title, api):
    ''' Checks the given title against the given API specifications to ensure it's short enough '''
    if len(title) > api.MAX_LIST_TITLE_LENGTH:
        raise ValueError("Title cannot be longer than {} characters".format(
            api.MAX_TASK_TITLE_LENGTH))


def _is_lists_of_digits(list_ids):
    ''' Checks the given list_ids contains only digits '''
    for item in list_ids:
        try:
            int(item)
        except ValueError:
            raise ValueError("List ids must contains only digits")


def get_folders(client):
    ''' Gets all the client's folders '''
    response = client.authenticated_request(client.api.Endpoints.FOLDERS)
    return response.json()


def get_folder(client, folder_id):
    ''' Gets the given list '''
    endpoint = '/'.join([client.api.Endpoints.FOLDERS, str(folder_id)])
    response = client.authenticated_request(endpoint)
    return response.json()


def create_folder(client, title, list_ids):
    ''' Creates a new list with the given title '''
    _check_title_length(title, client.api)
    _is_lists_of_digits(list_ids)
    data = {
        'title': title,
        'list_ids': list_ids
    }
    response = client.authenticated_request(client.api.Endpoints.FOLDERS,
                                            method='POST', data=data)
    return response.json()


def update_folder(client, folder_id, revision, title=None, list_ids=None):
    '''
    Updates the list with the given ID to have the given properties

    See https://developer.wunderlist.com/documentation/endpoints/list for detailed parameter information
    '''
    data = {
        'revision': revision,
    }

    if title:
        _check_title_length(title, client.api)
        data['title'] = title

    if list_ids:
        _is_lists_of_digits(list_ids)
        data['list_ids'] = list_ids

    endpoint = '/'.join([client.api.Endpoints.FOLDERS, str(folder_id)])
    response = client.authenticated_request(endpoint, 'PATCH', data=data)
    return response.json()


def delete_folder(client, folder_id, revision):
    params = {
        'revision': int(revision),
    }
    endpoint = '/'.join([client.api.Endpoints.FOLDERS, str(folder_id)])
    return client.authenticated_request(endpoint, 'DELETE', params=params)


def get_folder_revisions(client):
    response = client.authenticated_request(client.api.Endpoints.FOLDER_REVISIONS)
    return response.json()
