# $Id$
# Authority: dag
# Upstream: Ken Youens-Clark <kclark$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-RecordParser

Summary: Parse record-oriented data in a text file
Name: perl-Text-RecordParser
Version: 1.4.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-RecordParser/

Source: http://search.cpan.org/CPAN/authors/id/K/KC/KCLARK/Text-RecordParser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(Readonly)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(version)
Requires: perl(Class::Accessor)
Requires: perl(IO::Scalar)
Requires: perl(List::MoreUtils)
Requires: perl(List::Util)
Requires: perl(Readonly)
Requires: perl(version)

%filter_from_requires /^perl*/d
%filter_setup


%description
Parse record-oriented data in a text file.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
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
%doc Changes INSTALL MANIFEST META.yml README TODO
%doc %{_mandir}/man1/tablify.1*
%doc %{_mandir}/man1/tabmerge.1*
%doc %{_mandir}/man1/tab2graph.1*
%doc %{_mandir}/man3/Text::RecordParser.3pm*
%doc %{_mandir}/man3/Text::RecordParser::Tab.3pm*
%doc %{_mandir}/man3/Text::RecordParser::Object.3pm.gz
%{_bindir}/tablify
%{_bindir}/tabmerge
%{_bindir}/tab2graph
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/RecordParser/
%{perl_vendorlib}/Text/RecordParser.pm


%changelog
* Thu Mar 11 2010 Christoph Maser <cmr@financial.com> - 1.4.0-1
- Updated to version 1.4.0.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 1.3.0-1
- Updated to version 1.3.0.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Initial package. (using DAR)
