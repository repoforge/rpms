# $Id$
# Authority: dries
# Upstream: Mark Overmeer <mark$overmeer,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name OODoc

Summary: Creates code related documentation
Name: perl-OODoc
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/OODoc/

Source: http://search.cpan.org//CPAN/authors/id/M/MA/MARKOV/OODoc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Creates code related documentation in an object oriented way.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README LICENSE
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/oodist*
%{_bindir}/oodist
%{perl_vendorlib}/OODoc.p*
%{perl_vendorlib}/OODoc/

%changelog
* Thu Jul 5 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 1.01-1
- Updated to latest upstream version { old source not available }

* Wed Jan 10 2007 Dries Verachtert <dries@ulyssis.org> - 0.98-1
- Updated to release 0.98.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.94-1
- Initial package.
