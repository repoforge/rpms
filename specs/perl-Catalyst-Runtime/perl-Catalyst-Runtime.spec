# $Id$
# Authority: dag
# Upstream: Marcus Ramberg <mramberg$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Runtime

Summary: Catalyst  Runtime version
Name: perl-Catalyst-Runtime
Version: 5.7014
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Runtime/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Runtime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.1
### this module seems to require half of cpan..
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(CGI::Simple::Cookie)
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(Data::Dump)
BuildRequires: perl(File::Modified)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(HTTP::Body)
BuildRequires: perl(HTTP::Headers) >= 1.64
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Request::AsCGI)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Perl::Critic)
BuildRequires: perl(Text::SimpleTable)
BuildRequires: perl(Tree::Simple)
BuildRequires: perl(Tree::Simple::Visitor::FindByPath)
BuildRequires: perl(URI) >= 1.35
Requires: perl >= 2:5.8.1

%description
Catalyst Runtime version.

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
%doc %{_mandir}/man1/catalyst.pl.1*
%doc %{_mandir}/man3/Catalyst.3pm*
%doc %{_mandir}/man3/Catalyst::*.3pm*
%{_bindir}/catalyst.pl
%{perl_vendorlib}/Catalyst/
%{perl_vendorlib}/Catalyst.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 5.7014-1
- Updated to release 5.7014.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 5.7012-1
- Updated to release 5.7012.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 5.7011-1
- Updated to release 5.7011.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 5.7007-1
- Initial package. (using DAR)
