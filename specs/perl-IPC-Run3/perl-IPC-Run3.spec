# $Id$

# Authority: dries
# Upstream: Barrie Slaymaker <barries$slaysys,com>

%define real_name IPC-Run3
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Run a subprocess in batch mode
Name: perl-IPC-Run3
Version: 0.01
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-Run3/

Source: http://search.cpan.org/CPAN/authors/id/R/RB/RBS/IPC-Run3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Run a subprocess in batch mode.

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
%doc CHANGES
%doc %{_mandir}/man3/*
%{perl_vendorlib}/IPC/Run3.pm
%{perl_vendorlib}/IPC/Run3
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
