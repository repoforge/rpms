# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag$wieers,com>

%{?dist: %{expand: %%define %dist 1}}

%{?el4:%define _with_openoffice.org2 1}

Summary: Tool to convert between any document format supported by OpenOffice
Name: unoconv
Version: 0.2
Release: 1
License: GPL
Group: System Environment/Base
URL: http://dag.wieers.com/home-made/unoconv/

Source: http://dag.wieers.com/home-made/unoconv/unoconv-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.0
Requires: python >= 2.0
%{!?_with_openoffice.org2:Requires:openoffice.org-pyuno >= 2.0}
%{?_with_openoffice.org2:Requires:openoffice.org2-pyuno >= 2.0}

%description
unoconv converts between any document format that OpenOffice understands.
It uses OpenOffice's UNO bindings for non-interactive conversion of
documents.

Supported document formats include Open Document Format (.odf),
MS Word (.doc), MS Office Open/MS OOXML (.xml),
Portable Document Format (.pdf), HTML, XHTML, RTF, Docbook (.xml),
and more.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO WISHLIST docs/ tests/
%{_bindir}/unoconv

%changelog
* Sun May 20 2007 Dag Wieers <dag@wieers.com> - 0.2-1
- Updated to release 0.2.

* Sat May 19 2007 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
