# $Id$
# Authority: dag
# Upstream: Timothy Appnel <tima$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Atom-Syndication

Summary: Portable client for consuming RFC 4287 Atom Syndication Feeds
Name: perl-XML-Atom-Syndication
Version: 0.942
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Atom-Syndication/

Source: http://www.cpan.org/modules/by-module/XML/XML-Atom-Syndication-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
A portable client for consuming RFC 4287 Atom Syndication Feeds.

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
%doc %{_mandir}/man3/XML::Atom::Syndication.3pm*
%doc %{_mandir}/man3/XML::Atom::Syndication::*.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/Atom/
%{perl_vendorlib}/XML/Atom/Syndication/
%{perl_vendorlib}/XML/Atom/Syndication.pm

%changelog
* Mon Nov 10 2008 Dag Wieers <dag@wieers.com> - 0.942-1
- Initial package. (using DAR)
