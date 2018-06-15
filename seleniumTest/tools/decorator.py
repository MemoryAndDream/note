# -*- coding: utf-8 -*-
"""
File Name：     decorator
Description :
Author :       meng_zhihao
date：          2018/6/15
"""
def exception_retry(retry_times):
    def _decorator(view_func):
        def _wrapper_view(request, *args, **kwargs):
            for i in range(retry_times):
                try:
                    a = view_func(request, *args, **kwargs)
                    return a
                except Exception,e:
                    print str(e)
            return None
        return _wrapper_view
    return _decorator

