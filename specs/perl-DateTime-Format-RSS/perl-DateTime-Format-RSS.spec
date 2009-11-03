# $Id$
# Authority: shuff
# Upstream: Daisuke Maki <daisuke$endeworks,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-RSS

Summary: Format DateTime For RSS
Name: perl-%{real_name}
Version: 0.03000
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-RSS/

Source: http://search.cpan.org/CPAN/authors/id/D/DM/DMAKI/DateTime-Format-RSS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(DateTime::Format::DateParse)
BuildRequires: perl(DateTime::Format::ISO8601)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Install)
Requires: perl
Requires: perl(Class::Accessor::Fast)

%description
DateTime::Format::RSS attempts to deal with those nasty RSS date/time strings
used in fields (such as <issued>, <modified>, <pubDate>) that never ever seems
to be right.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/DateTime::Format::RSS.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Format/
%{perl_vendorlib}/DateTime/Format/RSS.pm

%changelog
* Thu Sep 24 2009 Steve Huff <shuff@vecna.org> - 0.03000-1
- Initial package.
