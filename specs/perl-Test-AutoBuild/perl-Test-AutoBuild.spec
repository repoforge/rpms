# $Id$
# Authority: dries
# Upstream: Daniel P. Berrangé <dan$berrange,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-AutoBuild

Summary: Automated build engine
Name: perl-Test-AutoBuild
Version: 1.0.3
Release: 1.2
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-AutoBuild/

Source: http://www.cpan.org/modules/by-module/Test/Test-AutoBuild-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker), perl-BSD-Resource

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
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGES INSTALL README
%doc %{_mandir}/man3/*.3pm*
%dir %{_sysconfdir}/auto-build.d/
%dir %{_sysconfdir}/auto-build.d/templates/
%config(noreplace) %{_sysconfdir}/auto-build.d/*
%{_bindir}/auto-build.pl
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/AutoBuild.pm
%{perl_vendorlib}/Test/AutoBuild/

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Updated to release 1.0.3.

* Sun Dec 19 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.2
- Initial package.
