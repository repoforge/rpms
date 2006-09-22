# $Id$
# Authority: dries
# Upstream: Philip Crow <philcrow2000$yahoo,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name UML-Sequence

Summary: Render UML sequence diagrams
Name: perl-UML-Sequence
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UML-Sequence/

Source: http://search.cpan.org//CPAN/authors/id/P/PH/PHILCROW/UML-Sequence-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
UML::Sequence and its helpers produce UML sequence diagrams.

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
%doc Changes README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/genericseq*
%doc %{_mandir}/man1/seq2rast*
%doc %{_mandir}/man1/seq2svg*
%{_bindir}/genericseq.pl
%{_bindir}/seq2rast.pl
%{_bindir}/seq2svg.pl
%{perl_vendorlib}/Devel/CallSeq.pm
%{perl_vendorlib}/Devel/OOCallSeq.pm
%{perl_vendorlib}/UML/Sequence.pm
%{perl_vendorlib}/UML/Sequence/
%{perl_vendorlib}/UML/genericseq.pl
%{perl_vendorlib}/UML/seq2rast.pl
%{perl_vendorlib}/UML/seq2svg.pl

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
