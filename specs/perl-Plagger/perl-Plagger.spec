# $Id$
# Authority: dag
# Upstream: Tatsuhiko Miyagawa <miyagawa@bulknews.net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Plagger
%define real_version 0.007017

Summary: Pluggable RSS/Atom Aggregator
Name: perl-Plagger
Version: 0.7.17
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Plagger/

Source: http://www.cpan.org/authors/id/M/MI/MIYAGAWA/Plagger-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.1
BuildRequires: perl(Cache::Cache) >= 1.04
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Date::Parse)
BuildRequires: perl(DateTime) >= 0.35
BuildRequires: perl(DateTime::Format::Mail) >= 0.32
BuildRequires: perl(DateTime::Format::Strptime)
BuildRequires: perl(DateTime::Format::W3CDTF)
BuildRequires: perl(DateTime::Locale) >= 0.32
BuildRequires: perl(DateTime::TimeZone) >= 0.56
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Encode) >= 2.1
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(HTML::Parser) >= 3.51
#BuildRequires: perl(HTML::ResolveLink)
BuildRequires: perl(LWP)
BuildRequires: perl(MIME::Types) >= 1.16
BuildRequires: perl(Module::Pluggable::Fast)
BuildRequires: perl(Net::DNS)
BuildRequires: perl(Template) >= 2.13
BuildRequires: perl(Template::Provider::Encoding) >= 0.04
BuildRequires: perl(Term::Encoding)
BuildRequires: perl(Test::Base) >= 0.52
BuildRequires: perl(Test::More) >= 0.42
BuildRequires: perl(Text::Tags)
BuildRequires: perl(UNIVERSAL::require) >= 0.1
BuildRequires: perl(URI::Fetch) >= 0.07
BuildRequires: perl(XML::Atom) >= 0.23
BuildRequires: perl(XML::Feed) >= 0.12
BuildRequires: perl(XML::LibXML)
BuildRequires: perl(XML::RSS::LibXML) >= 0.23
BuildRequires: perl(YAML) >= 0.39
BuildRequires: perl(YAML::Loader)
Requires: perl >= 2:5.8.1

%description
Pluggable RSS/Atom Aggregator.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changes MANIFEST META.yml examples/
%doc %{_mandir}/man3/Plagger.3pm*
#%{perl_vendorlib}/Plagger/
%{perl_vendorlib}/Plagger.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.7.17-1
- Initial package. (using DAR)
