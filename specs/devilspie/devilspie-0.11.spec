# $Id: devilspie.spec 3663 2005-10-20 04:38:29Z dries $
# Authority: dag
# Upstream: Ross Burton <ross$burtonini,com>

Summary: Window matching tool inspired by the Matched Window options in Sawfish
Name: devilspie
Version: 0.11
Release: 1%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://www.burtonini.com/blog/computers/devilspie/

Source: http://www.burtonini.com/computing/devilspie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gob2 >= 2.0.4, libwnck-devel, gtk2-devel, gettext
BuildRequires: libglade2-devel, intltool, perl-XML-Parser, libxslt

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
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING devilspie.dtd NEWS README TODO
%doc devilspie-reference.html sample-config.xml
%doc %{_mandir}/man1/devilspie.1*
%{_bindir}/devilspie

%changelog
* Tue Dec 20 2005 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

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
