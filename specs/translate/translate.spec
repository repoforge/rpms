# $Id$
# Authority: dries

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Aids with localization of software
Name: translate
Version: 0.8b1
Release: 1.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://translate.sourceforge.net/

Source: http://dl.sf.net/translate/translate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel

%description
Translate is a project to aid in localization of software. It deals with
conversion between different translation formats (such as gettext-based
.po formats, OpenOffice.org formats, and Mozilla formats). It also contains
tools to help process localizations etc.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{python_sitearch}/_csv.so
%{python_sitearch}/translate/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8b1-1.2
- Rebuild for Fedora Core 5.

* Sat May 23 2004 Dries Verachtert <dries@ulyssis.org> 0.8b1-1
- Initial package.
