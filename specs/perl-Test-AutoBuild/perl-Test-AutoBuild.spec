# $Id$

# Authority: dries
# Upstream: Daniel P. Berrangé <dan$berrange,com>

%define real_name Test-AutoBuild
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Automated build engine
Name: perl-Test-AutoBuild
Version: 1.0.2
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-AutoBuild/

Source: http://www.cpan.org/modules/by-module/Test/Test-AutoBuild-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Test-AutoBuild provides a PERL framework for performing
continuous, unattended, automated software builds.

  http://home.gna.org/testautobuild/

Pristine sources are checked out from a version control 
repository (currently has support for CVS, normal filesystem, 
Perforce & GNU Arch). A shell script (typically provided by
the application developer) is invoked to build the software 
and install it in a virtual root. Snapshots of the virtual 
root are taken before and after build to identify which 
files were installed. Snapshots of any designated 'package' 
directories are also taken to identify any RPM, Debian PKG, 
Tar, ZIP files which were built. Finally a set of output 
modules are run to generate HTML status page, copy packages 
and build logs to a Web / FTP server, send email notifications 
of build status, create ISO images.
 
The software is highly modularized and written in PERL to 
make it easily extendable to add new version control 
repositories, and output actions. It has no requirements 
around what build process an application uses (Make, 
autoconf, ANT, IMake), nor any requirements around the 
programming language used for the software. 


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README CHANGES AUTHORS INSTALL
%doc %{_mandir}/man3/*
%dir %{_sysconfdir}/auto-build.d
%dir %{_sysconfdir}/auto-build.d/templates
%config(noreplace) %{_sysconfdir}/auto-build.d/auto-build.*
%config(noreplace) %{_sysconfdir}/auto-build.d/*
%{_bindir}/auto-build.pl
%{perl_vendorlib}/Test/AutoBuild.pm
%{perl_vendorlib}/Test/AutoBuild/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/.packlist

# perl_vendorlib: /usr/lib/perl5/vendor_perl/5.8.0
# perl_vendorarch: /usr/lib/perl5/vendor_perl/5.8.0/i386-linux-thread-multi
# perl_archlib: /usr/lib/perl5/5.8.0/i386-linux-thread-multi
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Sun Dec 19 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.2
- Initial package.
