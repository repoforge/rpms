# $Id$

# Authority: dries
# Upstream: <autrijus$autrijus,org>

%{?dist: %{expand: %%define %dist 1}}

%define real_name ExtUtils-AutoInstall
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Automatic install of dependencies via CPAN
Name: perl-ExtUtils-AutoInstall
Version: 0.61
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-AutoInstall/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/ExtUtils-AutoInstall-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
%{?fc2:BuildRequires: perl-CPANPLUS}
%{?fc1:BuildRequires: perl-CPANPLUS}
%{?el3:BuildRequires: perl-CPANPLUS}

%description
ExtUtils::AutoInstall is a module to let Makefile.PL automatically 
install dependencies via CPAN or CPANPLUS.

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
%doc README Changes AUTHORS
%doc %{_mandir}/man3/*
%{perl_vendorlib}/ExtUtils/AutoInstall.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.61-1
- Initial package.
