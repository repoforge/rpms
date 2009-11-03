# $Id$
# Authority: vknecht

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

Summary: Generic Page Description Language parser
Name: pkpgcounter
Version: 3.20
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.pykota.com/software/pkpgcounter/

Source: http://www.pykota.com/software/pkpgcounter/download/tarballs/pkpgcounter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.2

Requires: python >= 2.2, python-imaging

#Provides: pkpgcounter
#Obsoletes: pkpgcounter <= %{version}-%{release}

%description
pkpgcounter is a generic Page Description Language parser which can either
compute the number of pages in a document, or compute the percent of
ink coverage needed to print each page, in different colorspaces.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS COPYING CREDITS NEWS README tests/
%doc %{_mandir}/man1/pkpgcounter.1*
%exclude %{_prefix}/share/doc/pkpgcounter
%{_bindir}/pkpgcounter
%{python_sitelib}/pkpgpdls/

%changelog
* Tue Oct 02 2007 Vincent Knecht <vknecht@users.sourceforge.net> - 3.20-1
- Updated for 3.20.

* Tue Aug 21 2007 Vincent Knecht <vknecht@users.sourceforge.net> - 2.18-1
- Initial packaging.
