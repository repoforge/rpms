# $Id$
# Authority: dries
# Upstream: Kevin Meltzer <perlguy$perlguy,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-TwoLevelHash

Summary: Tied interface to multi-dimensional (Two-Level) hash files
Name: perl-Tie-TwoLevelHash
Version: 1.2
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-TwoLevelHash/

Source: http://search.cpan.org/CPAN/authors/id/K/KM/KMELTZ/Tie-TwoLevelHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This is the Tie::TwoLevelHash module.  It is a TIEHASH interface which lets you
tie to a text file which is a multi-dimensional (two level) hash.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tie/TwoLevelHash.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Initial package.
