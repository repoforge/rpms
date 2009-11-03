# $Id$
# Authority: dries
# Upstream: Kirrily 'Skud' Robert <skud$infotrope,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAML-ConfigFile

Summary: Read configuration files in YAML format
Name: perl-YAML-ConfigFile
Version: 0.10
Release: 2.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-ConfigFile/

Source: http://www.cpan.org/modules/by-module/YAML/YAML-ConfigFile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module, you can read configuration files in YAML format.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} -pi -e 's|require v5.6.0.||g;' lib/YAML/ConfigFile.pm
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%{perl_vendorlib}/YAML/ConfigFile.pm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-2.2
- Rebuild for Fedora Core 5.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Requirements fixes.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
