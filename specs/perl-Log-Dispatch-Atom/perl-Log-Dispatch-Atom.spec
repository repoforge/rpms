# $Id$
# Authority: dries
# Upstream: Dominic Mitchell <cpan$happygiraffe,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Dispatch-Atom

Summary: Extend Log::Dispatch to allow logging to an Atom feed
Name: perl-Log-Dispatch-Atom
Version: 0.03
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Dispatch-Atom/

Source: http://search.cpan.org/CPAN/authors/id/H/HD/HDM/Log-Dispatch-Atom-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build

%description
This module extends Log::Dispatch to allow logging to an Atom feed.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Log/Dispatch/Atom.pm

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
