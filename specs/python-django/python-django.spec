# $Id$
# Authority: shuff

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define python_minver 2.3
%define major_release 1.2

%define real_name Django

Summary: The Web framework for perfectionists with deadlines
Name: python-django
Version: %{major_release}.3
Release: 2%{?dist}
License: BSD
Group: System Environment/Daemons
URL: http://www.djangoproject.com/

Source0: http://media.djangoproject.com/releases/%{major_release}/Django-%{version}.tar.gz
Source1: python-django.conf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel >= %{python_minver} 
BuildRequires: python >= %{python_minver} 
Requires: MySQL-python
Requires: python >= %{python_minver}
Requires: python-psycopg2
Requires: python-sqlite2 >= 2.0.3

Provides: django = %{version}-%{release}
Obsoletes: django <= %{version}-%{release}

%description
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design.

Developed four years ago by a fast-moving online-news operation, Django was
designed to handle two challenges: the intensive deadlines of a newsroom and
the stringent requirements of the experienced Web developers who wrote it. It
lets you build high-performing, elegant Web applications quickly.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

# Make a directory to hold Django apps
%{__install} -m0755 -d %{buildroot}%{_localstatedir}/www/django

# Install the Apache config
%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/httpd/conf.d/
%{__install} -m0644 %{_sourcedir}/python-django.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0775)
%doc AUTHORS INSTALL LICENSE README
%doc docs/ extras/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/python-django.conf
%{python_sitelib}/*
%{_bindir}/*

%defattr(0755, root, apache)
%dir %{_localstatedir}/www/django

%changelog
* Thu Oct 21 2010 Steve Huff <shuff@vecna.org> - 1.2.3-1
- Updated to version 1.2.3.
- No more examples/ directory.

* Tue Sep 21 2010 Steve Huff <shuff@vecna.org> - 1.1.1-2
- Renamed package to python-django.
- Removed mod_python dependency per Yury's suggestion.
- Django sites live in /var/www/django.

* Tue Apr 27 2010 Steve Huff <shuff@vecna.org> - 1.1.1-1
- Initial package.
