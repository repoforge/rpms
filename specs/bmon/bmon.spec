# $Id$
# Authority: dag

Summary: Console interface bandwidth usage monitor
Name: bmon
Version: 2.1.0
Release: 3
License: Artistic
Group: Applications/Internet
URL: http://people.suug.ch/~tgr/bmon/

Source: http://people.suug.ch/~tgr/bmon/files/bmon-%{version}.tar.gz
Patch0: bmon-2.1.0-shutdown.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Conflicts: nstats
BuildRequires: gettext, ncurses-devel, rrdtool-devel

%description
bmon is an interface bandwidth monitor.

%prep
%setup
%patch0 -p0

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog TODO
%doc %{_mandir}/man1/bmon.1*
%{_bindir}/bmon

%changelog
* Thu Dec 21 2006 Dag Wieers <dag@wieers.com> - 2.1.0-3
- Build fixes for gcc on at least FC6.

* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 2.1.0-2
- Fixed group.

* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 2.1.0-1
- Initial package. (using DAR)
