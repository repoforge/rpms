# $Id$

# Authority: dries
# Upstream: Kirrily 'Skud' Robert <skud$infotrope,net>

%define real_name YAML-ConfigFile
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Read configuration files in YAML format
Name: perl-YAML-ConfigFile
Version: 0.10
Release: 2.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-ConfigFile/

Source: http://www.cpan.org/modules/by-module/YAML/YAML-ConfigFile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
With this module, you can read configuration files in YAML format.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} -pi -e 's|require v5.6.0.||g;' lib/YAML/ConfigFile.pm
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
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
