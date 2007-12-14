# $Id$
# Authority: dries
# Upstream: Daniel P. Berrangé <dan$berrange,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-AutoBuild
%define real_version 1.002001

Summary: Automated build engine
Name: perl-Test-AutoBuild
Version: 1.2.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-AutoBuild/

Source: http://www.cpan.org/modules/by-module/Test/Test-AutoBuild-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
#BuildRequires: perl(BSD::Resource)
BuildRequires: perl(Class::MethodMaker)
BuildRequires: perl(Config::Record)
BuildRequires: perl(ExtUtils::MakeMaker)
Buildrequires: perl(Log::Log4perl)

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find doc/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGES INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml META.yml.PL README TODO doc/ examples/
%doc %{_mandir}/man1/auto-build.1*
%doc %{_mandir}/man1/auto-build-clean-root.1*
%doc %{_mandir}/man1/auto-build-make-root.1*
%doc %{_mandir}/man3/Test::AutoBuild.3pm*
%doc %{_mandir}/man3/Test::AutoBuild::*.3pm*
%doc %{_mandir}/man5/auto-build.conf.5*
#%config(noreplace) %{_sysconfdir}/auto-build.d/
%{_bindir}/auto-build
%{_bindir}/auto-build-clean-root
%{_bindir}/auto-build-make-root
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/AutoBuild/
%{perl_vendorlib}/Test/AutoBuild.pm

%changelog
* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Updated to release 1.0.3.

* Sun Dec 19 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.2
- Initial package.
