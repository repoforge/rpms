# $Id$
# Authority: dag
# Upstream: 

Summary: Tool to show progress of open files and file systems
Name: ftop
Version: 1.0
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://code.google.com/p/ftop/

Source: http://ftop.googlecode.com/files/ftop-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Ftop is to files what top is to processes. The progress of all open files and
file systems can be monitored. If run as a regular user, the set of open files
will be limited to those in that user's processes (which is generally all that
is of interest to the user). In any case, the selection of which files to
display is possible through a wide assortment of options. As with top, the
items are displayed in order from most to least active. 

%prep
%setup

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/ftop.1*
%{_bindir}/ftop

%changelog
* Sun Jun 27 2010 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
