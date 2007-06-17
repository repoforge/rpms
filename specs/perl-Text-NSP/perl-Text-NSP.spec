# $Id$
# Authority: dries
# Upstream: Ted Pedersen <tpederse$d,umn,edu>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-NSP

Summary: Ngram Statistics Package
Name: perl-Text-NSP
Version: 1.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-NSP/

Source: http://search.cpan.org//CPAN/authors/id/T/TP/TPEDERSE/Text-NSP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
The Ngram Statistics Package (NSP) is a suite of programs that aids in 
analyzing Ngrams in text files. We define an Ngram as a sequence of 'n' 
tokens that occur within a window of at least 'n' tokens in the text; 
what constitutes a "token" can be defined by the user.

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
%doc CHANGES README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/combig-script.sh
%{_bindir}/combig.pl
%{_bindir}/count.pl
%{_bindir}/huge-combine.pl
%{_bindir}/huge-count.pl
%{_bindir}/kocos-script.sh
%{_bindir}/kocos.pl
%{_bindir}/rank-script.sh
%{_bindir}/rank.pl
%{_bindir}/sort-bigrams.pl
%{_bindir}/split-data.pl
%{_bindir}/statistic.pl
%{perl_vendorlib}/Text/NSP.pm
%{perl_vendorlib}/Text/NSP/

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
