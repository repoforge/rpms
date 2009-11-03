# $Id$
# Authority: dries
# Upstream: Troels Liebe Bentsen <tlb$rapanden,dk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name RPM-Perlonly

Summary: Perl only implementaion of a RPM header reader
Name: perl-RPM-Perlonly
Version: 1.0.1
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RPM-Perlonly/

Source: http://search.cpan.org/CPAN/authors/id/T/TL/TLBDK/RPM-Perlonly-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl-RPM-Perlonly is a clone of RPM::Header written in only perl, so it provides
a way to read a rpm package on systems where rpm is installed. Perl-RPM-Perlonly
can used as a drop in replacement for RPM::Header, if needed also the other way
around.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/RPM/Perlonly.pm
%{perl_vendorlib}/RPM/Tagtable.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Initial package.
