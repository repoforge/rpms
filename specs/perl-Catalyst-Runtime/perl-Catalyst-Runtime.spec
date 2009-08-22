# $Id$
# Authority: dag
# Upstream: Marcus Ramberg <mramberg$cpan,org>
# Needs new MooseX::*
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Runtime

Summary: Catalyst  Runtime version
Name: perl-Catalyst-Runtime
Version: 5.80010
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Runtime/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Catalyst-Runtime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Exception)
# From yaml requires
BuildRequires: perl(B::Hooks::EndOfScope) >= 0.08
BuildRequires: perl(CGI::Simple::Cookie)
BuildRequires: perl(Carp)
BuildRequires: perl(Class::C3::Adopt::NEXT) >= 0.07
BuildRequires: perl(Class::MOP) >= 0.83
BuildRequires: perl(Data::Dump)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(HTTP::Body) >= 1.04
BuildRequires: perl(HTTP::Headers) >= 1.64
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Request::AsCGI) >= 0.8
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Module::Pluggable) >= 3.9
BuildRequires: perl(Moose) >= 0.78
BuildRequires: perl(MooseX::Emulate::Class::Accessor::Fast) >= 0.00801
BuildRequires: perl(MooseX::MethodAttributes::Inheritable) >= 0.15
BuildRequires: perl(Path::Class) >= 0.09
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(String::RewritePrefix) >= 0.004
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Text::Balanced)
BuildRequires: perl(Text::SimpleTable) >= 0.03
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(Tree::Simple) >= 1.15
BuildRequires: perl(Tree::Simple::Visitor::FindByPath)
BuildRequires: perl(URI) >= 1.35
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(namespace::clean)
BuildRequires: perl >= 5.8.6
BuildRequires: perl(B::Hooks::OP::Check::StashChange)
Provides:      perl(Catalyst::Engine::HTTP::Restarter)
Provides:      perl(Catalyst::Engine::HTTP::Restarter::Watcher)


%description
Catalyst Runtime version.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 5.80010-1
- Updated to version 5.80010.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 5.7015-1
- Updated to release 5.7015.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 5.7014-1
- Updated to release 5.7014.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 5.7012-1
- Updated to release 5.7012.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 5.7011-1
- Updated to release 5.7011.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 5.7007-1
- Initial package. (using DAR)
