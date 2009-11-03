# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name twill

Summary: Simple scripting language for Web browsing
Name: python-twill
Version: 0.9
Release: 1%{?dist}
License: MIT
Group: Applications/Internet
URL: http://twill.idyll.org/

Source: http://darcs.idyll.org/~t/projects/twill-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools

%description
twill is a simple language that allows users to browse the Web from a
command-line interface. With twill, you can navigate through Web sites that
use forms, cookies, and most standard Web features.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}" \
    --single-version-externally-managed

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.txt doc/ChangeLog doc/*.txt
%{_bindir}/twill-fork
%{_bindir}/twill-sh
%{python_sitelib}/twill/
%{python_sitelib}/twill-*.egg-info/

%changelog
* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.9-1
- Updated to release 0.9.

* Tue Oct 21 2008 Matthias Saou <http://freshrpms.net/> 0.9-0.2
- Update to 0.9 final.
- Rename from twill to python-twill.

* Sat Aug 18 2007 Luke Macken <lmacken@redhat.com> - 0.9-0.1.b1
- Initial creation

