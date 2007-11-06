# $Id$
# Authority: dries
# Upstream: Michael G Schwern <mschwern$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-Cache-LRU

Summary: Least-Recently Used cache
Name: perl-Tie-Cache-LRU
Version: 0.21
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-Cache-LRU/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/Tie-Cache-LRU-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
A Least-Recently Used cache.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tie/Cache/LRU.pm
%{perl_vendorlib}/Tie/Cache/LRU

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.21-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Initial package.
