# $Id$
# Authority: dag
# Upstream: Ross Burton <ross$burtonini,com>

Summary: Window matching tool inspired by the Matched Window options in Sawfish
Name: devilspie
Version: 0.22
Release: 1
License: GPL
Group: User Interface/Desktops
URL: http://www.burtonini.com/blog/computers/devilspie/

Source: http://www.burtonini.com/computing/devilspie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gob2 >= 2.0.4, libwnck-devel, gtk2-devel, gettext
BuildRequires: libglade2-devel, intltool, perl-XML-Parser, libxslt
BuildRequires: glib2-devel >= 2.9.1

%description
A window-matching utility, inspired by Sawfish's "Matched Windows" option and
the lack of the functionality in Metacity. Metacity lacking window matching is
not a bad thing -- Metacity is a lean window manager, and window matching does
not have to be a window manager task.

Devil's Pie can be configured to detect windows as they are created, and match
the window to a set of rules. If the window matches the rules, it can perform a
series of actions on that window. For example, I make all windows created by
X-Chat appear on all workspaces, and the main Gkrellm1 window does not appear
in the pager or task list.

%prep
%setup

%build
%configure
%{__make} clean
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO tests/
%doc %{_mandir}/man1/devilspie.1*
%{_bindir}/devilspie

%changelog
* Thu Jan 03 2008 Dag Wieers <dag@wieers.com> - 0.22-1
- Updated to release 0.22.

* Mon Jun 25 2007 Dag Wieers <dag@wieers.com> - 0.20.2-1.
- Updated to release 0.20.2.

* Thu Feb 01 2007 Dag Wieers <dag@wieers.com> - 0.20.1-1.
- Updated to release 0.20.1.

* Fri Dec 22 2006 Dag Wieers <dag@wieers.com> - 0.19-1
- Updated to release 0.19.

* Sat Mar 18 2006 Dag Wieers <dag@wieers.com> - 0.17.1-1
- Updated to release 0.17.1.

* Tue Dec 20 2005 Dag Wieers <dag@wieers.com> - 0.16-1
- Updated to release 0.16.

* Mon Aug 08 2005 Dag Wieers <dag@wieers.com> - 0.10-2
- Added devilspie-reference.html to documentation. (Anthony Caetano)

* Thu Jul 14 2005 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Mon Feb 14 2005 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Sat Nov 13 2004 Dag Wieers <dag@wieers.com> - 0.7-1
- Updated to release 0.7.

* Sun Oct 19 2003 Dag Wieers <dag@wieers.com> - 0.3.1-0
- Updated to release 0.3.1.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.2.4-0
- Initial package. (using DAR)
