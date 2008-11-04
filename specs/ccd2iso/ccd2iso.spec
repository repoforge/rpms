# $Id$
# Authority: dag

Summary: CloneCD image to ISO image converter
Name: ccd2iso
Version: 0.3
Release: 1
License: GPL
Group: Applications/File
URL: http://ccd2iso.sourceforge.net/

Source: http://dl.sf.net/ccd2iso/ccd2iso-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: dos2unix

%description
CloneCD image to ISO image converter.

%prep
%setup

dos2unix AUTHORS COPYING ChangeLog README TODO
%{__chmod} 644 AUTHORS COPYING ChangeLog README TODO

%build
autoreconf -fi
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/ccd2iso

%changelog
* Wed Nov 05 2008 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
