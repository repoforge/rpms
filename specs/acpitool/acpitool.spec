# $Id$
# Authority: dries
# Upstream: DLeemans <d_leemans$telenet,be>

Summary: Command line ACPI client
Name: acpitool
Version: 0.5
Release: 1
License: GPL
Group: Applications/System
URL: http://freeunix.dyndns.org:8000/site2/acpitool.shtml

Source: http://freeunix.dyndns.org:8000/ftp_site/pub/unix/acpitool/acpitool-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
AcpiTool is a Linux ACPI client. It's a small command line application, 
intended to be a replacement for the apm tool. The primary target audience 
are laptop users, since these people are most interested in things like 
battery status, thermal status and the ability to suspend (sleep mode). 
The program simply accesses the /proc/acpi or /sysfs entries to get or set 
ACPI values.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/acpitool*
%{_bindir}/acpitool

%changelog
* Fri Jul 25 2008 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Updated to release 0.5.

* Tue Feb 13 2007 Dries Verachtert <dries@ulyssis.org> - 0.4.7-1
- Updated to release 0.4.7.

* Thu Aug 10 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.6-1
- Initial package.
