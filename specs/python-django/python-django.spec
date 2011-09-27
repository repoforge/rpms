# $Id$
# Authority: shuff
# Upstream: Django Software Foundation <foundation$djangoproject,com>

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%global python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%endif

%{?el5:%global _without_egginfo 1}

%global python_minver 2.4
%global major_release 1.3

%global real_name Django

Summary: The Web framework for perfectionists with deadlines
Name: python-django
Version: %{major_release}.1
Release: 1%{?dist}
License: BSD
Group: Development/Languages
URL: http://www.djangoproject.com/

Source0: http://media.djangoproject.com/releases/%{major_release}/Django-%{version}.tar.gz
Source1: python-django.conf
Source2: python-django.wsgi

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel >= %{python_minver}
Requires: python >= %{python_minver}

Provides: Django = %{version}-%{release}
Obsoletes: Django < 1.3.1-1, django < 1.3.1-1

%description
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design.

Developed four years ago by a fast-moving online-news operation, Django was
designed to handle two challenges: the intensive deadlines of a newsroom and
the stringent requirements of the experienced Web developers who wrote it. It
lets you build high-performing, elegant Web applications quickly.

%package integration-apache
Summary: The Web framework for perfectionists with deadlines (Apache integration)
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

# Apache web server, obviously
Requires: httpd

# Corresponding Apache modules
%{?el5:Requires: mod_python}
%{?el6:Requires: mod_wsgi}

# MySQL (ships with RHEL)
Requires: MySQL-python

# PostgreSQL (RepoForge for RHEL <=5, stock for RHEL6)
Requires: python-psycopg2

# SQLite (RepoForge for RHEL5, stock for RHEL6)
%{?el5:Requires: python-sqlite2}
%{?el6:Requires: python-sqlite}

%description integration-apache
This package provides Apache integration for Django.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}

%{__python} setup.py install --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

# W: doc-file-dependency
rm docs/ref/contrib/gis/create_template_postgis*.sh

# Handling locale files
(cd %{buildroot} && find . -name 'django*.mo') | %{__sed} -e 's|^.||' | %{__sed} -e \
    's:\(.*/locale/\)\([^/_]\+\)\(.*\.mo$\):%lang(\2) \1\2\3:' \
    >> %{name}.lang

# install man pages
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p docs/man/* %{buildroot}%{_mandir}/man1/

# Fix items in %%{_bindir}
mv %{buildroot}%{_bindir}/django-admin.py %{buildroot}%{_bindir}/django-admin

# remove .po files
find %{buildroot} -name "*.po" | xargs rm -f

# Fix permissions
chmod 755 \
    %{buildroot}%{python_sitelib}/django/contrib/admin/media/js/compress.py \

# Bash completion
install -d %{buildroot}%{_sysconfdir}/bash_completion.d/
install -m 0644 extras/django_bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/django
rm extras/django_bash_completion

# Install the Apache config
%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/httpd/conf.d/django
%{__install} -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/django.conf
%{__install} -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/httpd/conf.d/django/default.wsgi

# Make a directory to hold Django apps
%{__install} -m0755 -d %{buildroot}%{_localstatedir}/www/django/

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS LICENSE PKG-INFO README
%doc docs/ extras/
%{_bindir}/django-admin
%{_mandir}/man1/*
%config %{_sysconfdir}/bash_completion.d/django
%{python_sitelib}/django/*.py*
%{python_sitelib}/django/bin/__init__.py*
%{python_sitelib}/django/bin/profiling/__init__.py*
%attr(0755,root,root) %{python_sitelib}/django/bin/daily_cleanup.py
%attr(0755,root,root) %{python_sitelib}/django/bin/django-admin.py
%attr(0755,root,root) %{python_sitelib}/django/bin/unique-messages.py
%attr(0755,root,root) %{python_sitelib}/django/bin/profiling/gather_profile_stats.py
%{python_sitelib}/django/bin/daily_cleanup.py?
%{python_sitelib}/django/bin/django-admin.py?
%{python_sitelib}/django/bin/unique-messages.py?
%{python_sitelib}/django/bin/profiling/gather_profile_stats.py?
%{python_sitelib}/django/conf/*.py*
%{python_sitelib}/django/conf/app_template/
%{python_sitelib}/django/conf/locale/*.py*
%{python_sitelib}/django/conf/locale/*/*.py*
%attr(0755,root,root) %{python_sitelib}/django/conf/project_template/manage.py
%{python_sitelib}/django/conf/project_template/manage.py?
%{python_sitelib}/django/conf/project_template/__init__.py*
%{python_sitelib}/django/conf/project_template/settings.py*
%{python_sitelib}/django/conf/project_template/urls.py*
%{python_sitelib}/django/conf/urls/
%{python_sitelib}/django/contrib/*.py*
%{python_sitelib}/django/contrib/*/*.py*
%{python_sitelib}/django/contrib/*/fixtures/
%{python_sitelib}/django/contrib/*/handlers/
%{python_sitelib}/django/contrib/*/management/
%{python_sitelib}/django/contrib/*/media/
%{python_sitelib}/django/contrib/*/plugins/
%{python_sitelib}/django/contrib/*/templates/
%{python_sitelib}/django/contrib/*/templatetags/
%{python_sitelib}/django/contrib/*/tests/
%{python_sitelib}/django/contrib/*/views/
%{python_sitelib}/django/contrib/gis/*maps/
%{python_sitelib}/django/contrib/gis/admin/
%{python_sitelib}/django/contrib/gis/db/
%{python_sitelib}/django/contrib/gis/forms/
%{python_sitelib}/django/contrib/gis/g*/
%{python_sitelib}/django/contrib/gis/utils/
%{python_sitelib}/django/contrib/localflavor/??/
%{python_sitelib}/django/contrib/localflavor/??_/
%{python_sitelib}/django/contrib/localflavor/generic/
%{python_sitelib}/django/contrib/messages/storage/
%{python_sitelib}/django/contrib/sessions/backends/
%{python_sitelib}/django/core/
%{python_sitelib}/django/db/
%{python_sitelib}/django/dispatch/
%{python_sitelib}/django/forms/
%{python_sitelib}/django/http/
%{python_sitelib}/django/middleware/
%{python_sitelib}/django/shortcuts/
%{python_sitelib}/django/template/
%{python_sitelib}/django/templatetags/
%{python_sitelib}/django/test/
%{python_sitelib}/django/utils/
%{python_sitelib}/django/views/
%{!?_without_egginfo:%{python_sitelib}/*.egg-info}

%files integration-apache
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/httpd/conf.d/django.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/django/default.wsgi
%{_localstatedir}/www/django/

%changelog
* Tue Sep 27 2011 Yury V. Zaytsev <yury@shurup.com> - 1.3.1-1
- Updated to release 1.3.1.
- Split Apache integration files in a sub-package.

* Thu Oct 21 2010 Steve Huff <shuff@vecna.org> - 1.2.3-1
- Updated to version 1.2.3.
- No more examples/ directory.

* Tue Sep 21 2010 Steve Huff <shuff@vecna.org> - 1.1.1-2
- Renamed package to python-django.
- Removed mod_python dependency per Yury's suggestion.
- Django sites live in /var/www/django.

* Tue Apr 27 2010 Steve Huff <shuff@vecna.org> - 1.1.1-1
- Initial package.
