# $Id$
# Authority: dag
# Upstream: Six Apart <cpan@sixapart.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Feed

Summary: XML Syndication Feed Support
Name: perl-XML-Feed
Version: 0.43
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Feed/

Source: http://www.cpan.org/modules/by-module/XML/XML-Feed-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::ErrorHandler)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::Mail)
BuildRequires: perl(DateTime::Format::W3CDTF)
BuildRequires: perl(Feed::Find)
BuildRequires: perl(Module::Build)
BuildRequires: perl(HTML::TokeParser)
#BuildRequires: perl(List:Util)
BuildRequires: perl(LWP)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::Fetch)
BuildRequires: perl(XML::Atom) >= 0.08
BuildRequires: perl(XML::RSS) >= 1.01

%description
XML Syndication Feed Support.

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
%doc %{_mandir}/man3/XML::Feed.3pm*
%doc %{_mandir}/man3/XML::Feed::*.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Feed/
%{perl_vendorlib}/XML/Feed.pm

%changelog
* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.43-1
- Updated to version 0.43.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
