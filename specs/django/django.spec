# $Id$
# Authority: shuff

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define python_minver 2.3

%define real_name Django

Summary: The Web framework for perfectionists with deadlines
Name: django
Version: 1.1.1
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
URL: http://www.djangoproject.com/

Source0: http://media.djangoproject.com/releases/%{version}/Django-%{version}.tar.gz
Source1: python-django.conf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel >= %{python_minver} 
BuildRequires: python >= %{python_minver} 
Requires: mod_python
Requires: MySQL-python
Requires: python >= %{python_minver}
Requires: python-psycopg2
Requires: python-sqlite2 >= 2.0.3

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
%{__install} -m0755 -d %{buildroot}%{_datadir}/django

# Install the Apache config
%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/httpd/conf.d/
%{__install} -m0644 %{_sourcedir}/python-django.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0775)
%doc AUTHORS INSTALL LICENSE README
%doc docs/ examples/ extras/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/python-django.conf
%{python_sitelib}/*
%{_bindir}/*

%defattr(0755, root, apache)
%dir %{_datadir}/django

%changelog
* Tue Apr 27 2010 Steve Huff <shuff@vecna.org> - 1.1.1-1
- Initial package.
