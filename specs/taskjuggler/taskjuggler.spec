# $Id$
# Authority: dries
# Upstream: Chris Schlaeger <cs$kde,org>

### EL6 ships with taskjuggler-2.4.3-5.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Project management tool
Name: taskjuggler
Version: 2.4.0
Release: 1%{?dist}
License: GPL
Group: Applications/Utilities
URL: http://www.taskjuggler.org/

Source: http://www.taskjuggler.org/download/taskjuggler-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++, kdepim-devel, docbook-dtds, gettext

%description
TaskJuggler is a modern and powerful project management tool. Its new approach
to project planning and tracking is far superior to the commonly used Gantt
chart editing tools. It has already been successfully used in many projects
and scales easily to projects with hundreds of resources and thousands of
tasks. It covers the complete spectrum of project management tasks from the
first idea to the completion of the project. It assists you during project
scoping, resource assignment, cost and revenue planing, and risk and
communication management.

%prep
%setup
%{__perl} -pi -e "s|/usr/share/xml/docbook/schema/dtd/4.3/docbookx.dtd|/usr/share/sgml/docbook/xml-dtd-4.3-1.0-26/docbookx.dtd|g;" docs/en/*

%build
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__perl} -pi -e "s|^docprefix = /usr|docprefix=\\$\(prefix\)|g;" docs/en/Makefile
%{__make} install DESTDIR=%{buildroot}
%{__mv} %{buildroot}%{_datadir}/doc/packages/taskjuggler rpmdocs
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO rpmdocs/*
%{_libdir}/libtaskjuggler.so*
%{_libdir}/libtaskjuggler.la
%{_datadir}/config/taskjugglerrc
%{_datadir}/apps/katepart/syntax/taskjuggler.xml
%{_datadir}/apps/taskjuggler/
%{_datadir}/mimelnk/application/x-tj?.desktop
%{_datadir}/applications/kde/taskjuggler.desktop
%{_datadir}/doc/HTML/*/taskjuggler/
%{_datadir}/icons/*/*/*/taskjuggler*.png
%{_bindir}/taskjuggler
%{_bindir}/TaskJugglerUI

%changelog
* Tue Jul 10 2007 Dries Verachtert <dries@ulyssis.org> - 2.4.0-1
- Updated to release 2.4.0.

* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 2.3.1-1
- Updated to release 2.3.1.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.3.0-1
- Updated to release 2.3.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.0-1.2
- Rebuild for Fedora Core 5.

* Tue Dec 27 2005 Dries Verachtert <dries@ulyssis.org> - 2.2.0-1
- Initial package.
