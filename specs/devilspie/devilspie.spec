# $Id$

# Authority: dag
# Upstream: Ross Burton <ross@burtonini.com>

Summary: Window matching tool inspired by the Matched Window options in Sawfish
Name: devilspie
Version: 0.3.1
Release: 0
License: GPL
Group: User Interface/Desktops
URL: http://www.burtonini.com/blog/computers/devilspie/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.burtonini.com/computing/devilspie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gob2 >= 2.0.4, libwnck-devel, libglade-devel, gtk2-devel

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
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README NEWS TODO sample-config.xml devilspie.dtd
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sun Oct 19 2003 Dag Wieers <dag@wieers.com> - 0.3.1-0
- Updated to release 0.3.1.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.2.4-0
- Initial package. (using DAR)
