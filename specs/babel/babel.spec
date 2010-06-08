# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name Babel

Summary: Tools for internationalizing Python applications
Name: babel
Version: 0.9.5
Release: 1%{?dist}
License: BSD
Group: Development/Languages
URL: http://babel.edgewall.org/

Source: http://ftp.edgewall.com/pub/babel/Babel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools-devel
Requires: python-babel
Requires: python-setuptools

%description
Babel is composed of two major parts:

* tools to build and work with gettext message catalogs

* a Python interface to the CLDR (Common Locale Data Repository),
  providing access to various locale display names, localized number
  and date formatting, etc.

%package -n python-babel
Summary: Library for internationalizing Python applications
Group: Development/Languages

%description -n python-babel
Babel is composed of two major parts:

* tools to build and work with gettext message catalogs

* a Python interface to the CLDR (Common Locale Data Repository),
  providing access to various locale display names, localized number
  and date formatting, etc.

%prep
%setup -n %{real_name}-%{version}
chmod a-x babel/messages/frontend.py doc/logo.png doc/logo_small.png
%{__sed} -i -e '/^#!/,1d' babel/messages/frontend.py

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
 
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README.txt doc/cmdline.txt
%{_bindir}/pybabel

%files -n python-babel
%defattr(-, root, root, 0755)
%doc doc/
%{python_sitelib}/*

%changelog
* Mon Jun 07 2010 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Initial package. (using DAR)
