# $Id$
# Authority: dag

Summary: Console interface bandwidth usage monitor
Name: bmon
Version: 2.1.0
Release: 2.2
License: Artistic
Group: Applications/Internet
URL: http://people.suug.ch/~tgr/bmon/

Source: http://people.suug.ch/~tgr/bmon/files/bmon-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Conflicts: nstats
#BuildRequires: gettext-devel
BuildRequires: gettext, ncurses-devel, rrdtool-devel

%description
bmon is an interface bandwidth monitor.

%prep
%setup

%build
#%{__gettextize}
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
#%{__install} -Dp -m0755 bmon %{buildroot}%{_bindir}/bmon
#%{__install} -Dp -m0644 bmon.1 %{buildroot}%{_mandir}/man1/bmon.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog TODO
%doc %{_mandir}/man1/bmon.1*
%{_bindir}/bmon

%changelog
* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 2.1.0-2
- Fixed group.

* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 2.1.0-1
- Initial package. (using DAR)
