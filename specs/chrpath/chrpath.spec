# $Id$
# Authority: dag

Summary: Change the dynamic library load path (rpath) of binaries
Name: chrpath
Version: 0.13
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: ftp://ftp.hungry.com/pub/hungry/chrpath/

Source: ftp://ftp.hungry.com/pub/hungry/chrpath/chrpath-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs. Currently, only removing and modifying the rpath
is supported. Eventually, I hope to be able to add an rpath if it is
missing.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/chrpath.1*
%{_bindir}/chrpath
%exclude %{_prefix}/doc/

%changelog
* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Tue Sep 16 2003 Dag Wieers <dag@wieers.com> - 0.11-0
- Updated to release 0.11.

* Tue Aug 19 2003 Dag Wieers <dag@wieers.com> - 0.10-0
- Initial package. (using DAR)
