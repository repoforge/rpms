# $Id$
# Authority: dries
# Upstream: &#1497;&#1493;&#1489;&#1500; &#1511;&#1493;&#1490;'&#1502;&#1503; <nothingmuch$woobling,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name UNIVERSAL-isa

Summary: Hack around people using UNIVERSAL::isa
Name: perl-UNIVERSAL-isa
Version: 0.05
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UNIVERSAL-isa/

Source: http://search.cpan.org/CPAN/authors/id/N/NU/NUFFIN/UNIVERSAL-isa-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Hack around module authors using UNIVERSAL::isa as a function when they shouldn't.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%{perl_vendorlib}/UNIVERSAL/isa.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1.2
- Rebuild for Fedora Core 5.

* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
