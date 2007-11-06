# $Id$
# Authority: dries
# Upstream: Tom Scanlan <cutthis,tscanlan$sosaith,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AI-Fuzzy

Summary: Perl extension for Fuzzy Logic
Name: perl-AI-Fuzzy
Version: 0.05
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AI-Fuzzy/

Source: http://search.cpan.org/CPAN/authors/id/T/TS/TSCANLAN/AI-Fuzzy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
AI::Fuzzy really consists of two modules - AI::Fuzzy::Label and
AI::Fuzzy::Set.

A fuzzy set is simply a mathematical set to which members can
*partially* belong. For example, a particular shade of gray may
partially belong to the set of dark colors, whereas black would have
full membership, and lemon yellow would have almost no membership.

A fuzzy labeler classifies a particular crisp value by examining the
degree to which it belongs to several sets, and selecting the most
appropriate. For example, it can decide whether to call water at 60
degrees Farenheight "cold", "cool", or "warm". A fuzzy label might be
one of these labels, or a fuzzy set describing to what degree each of
the labels describes the particular value in question.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/AI/Fuzzy.pm
%{perl_vendorlib}/AI/Fuzzy

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
