# $Id$
# Authority: pdurbin
# Upstream: Kees Cook <kees$outflux,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name gsh

Summary: Global Shell run commands in parallel to multiple machines
Name: gsh
Version: 1.0.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://outflux.net/unix/software/gsh/

Source: http://outflux.net/unix/software/gsh/download/gsh-%{version}.tar.gz
Patch0: gsh-intersection.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(File::Temp)
Requires: perl(Getopt::Long)
Requires: perl(POSIX)
Requires: perl(Pod::Usage)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
The idea behind this tool originally came from wanting to do something
on each machine in our network.  Existing scripts would serially go to
each machine run the command, wait for it to finish, and continue to
the next machine.  There was no reason why this couldn’t be done in
parallel.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog META.yml README TODO
%doc %{_mandir}/man?/*
/usr/bin/ghosts
/usr/bin/gsh
%{perl_vendorlib}/SystemManagement/Ghosts.pm
%exclude %{perl_vendorarch}/auto/*/.packlist

%changelog
* Fri Apr 29 2011 Philip Durbin <philipdurbin@gmail.com> 1.0.2-1
- Initial package
- Includes intersections patch from Mark D. Nagel.
