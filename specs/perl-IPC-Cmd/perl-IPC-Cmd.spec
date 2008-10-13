# $Id$
# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPC-Cmd

Summary: Finding and running system commands made easy
Name: perl-IPC-Cmd
Version: 0.42
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-Cmd/

Source: http://www.cpan.org/modules/by-module/IPC/IPC-Cmd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Allows for the searching and execution of any binary on your system.
It adheres to verbosity settings and is able to run intereactive. It
also has an option to capture output/error buffers.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/IPC::Cmd.3pm*
%dir %{perl_vendorlib}/IPC/
%{perl_vendorlib}/IPC/Cmd.pm

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.42-1
- Updated to release 0.42.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.40-1
- Updated to release 0.40.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.36-1
- Updated to release 0.36.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.34-1
- Updated to release 0.34.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Updated to release 0.25.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Initial package.
