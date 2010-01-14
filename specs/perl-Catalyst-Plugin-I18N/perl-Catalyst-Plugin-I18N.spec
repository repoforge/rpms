# $Id$
# Authority: cmr
# Upstream: Marcus Ramberg <mramberg@cpan.org>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-I18N

Summary: I18N for Catalyst
Name: perl-Catalyst-Plugin-I18N
Version: 0.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-I18N/

Source: http://search.cpan.org/CPAN/authors/id/M/MR/MRAMBERG/Catalyst-Plugin-I18N-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(I18N::LangTags) >= 0.35
BuildRequires: perl(Locale::Maketext::Lexicon)
BuildRequires: perl(Locale::Maketext::Simple)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.8.0
Requires: perl(Catalyst::Runtime)
Requires: perl(I18N::LangTags) >= 0.35
Requires: perl(Locale::Maketext::Lexicon)
Requires: perl(Locale::Maketext::Simple)
Requires: perl(MRO::Compat)
Requires: perl >= 5.8.0

%filter_from_requires /^perl*/d
%filter_setup


%description
I18N for Catalyst.

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
%doc %{_mandir}/man3/Catalyst::Plugin::I18N.3pm*
%doc %{_mandir}/man3/Catalyst::Plugin::I18N::Manual.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%{perl_vendorlib}/Catalyst/Plugin/I18N.pm
%{perl_vendorlib}/Catalyst/Plugin/I18N/Manual.pod

%changelog
* Thu Jan 14 2010 Christoph Maser <cmr@financial.com> - 0.09-1
- Initial package. (using DAR)
