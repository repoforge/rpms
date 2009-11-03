# $Id$
# Authority: dries
# Upstream: Philip Crow <crow,phil$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UML-Sequence

Summary: Render UML sequence diagrams
Name: perl-UML-Sequence
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UML-Sequence/

Source: http://www.cpan.org/modules/by-module/UML/UML-Sequence-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
UML::Sequence and its helpers produce UML sequence diagrams.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man1/genericseq.pl.1*
%doc %{_mandir}/man1/seq2rast.pl.1*
%doc %{_mandir}/man1/seq2svg.pl.1*
%doc %{_mandir}/man3/Devel::CallSeq.3pm*
%doc %{_mandir}/man3/Devel::OOCallSeq.3pm*
%doc %{_mandir}/man3/UML::Sequence.3pm*
%doc %{_mandir}/man3/UML::Sequence::*.3pm*
%doc %{_mandir}/man3/UML::genericseq.3pm*
%doc %{_mandir}/man3/UML::seq2rast.3pm*
%doc %{_mandir}/man3/UML::seq2svg.3pm*
%{_bindir}/genericseq.pl
%{_bindir}/seq2rast.pl
%{_bindir}/seq2svg.pl
%dir %{perl_vendorlib}/Devel/
%{perl_vendorlib}/Devel/CallSeq.pm
%{perl_vendorlib}/Devel/OOCallSeq.pm
%dir %{perl_vendorlib}/UML/
%{perl_vendorlib}/UML/Sequence/
%{perl_vendorlib}/UML/Sequence.pm
%{perl_vendorlib}/UML/genericseq.pl
%{perl_vendorlib}/UML/seq2rast.pl
%{perl_vendorlib}/UML/seq2svg.pl

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
