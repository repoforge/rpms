# $Id$
# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-RSS-TimingBotDBI

Summary: XML::RSS::TimingBot-subclass that saves state with DBI
Name: perl-XML-RSS-TimingBotDBI
Version: 2.01
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-RSS-TimingBotDBI/

Source: http://www.cpan.org/modules/by-module/XML/XML-RSS-TimingBotDBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This class is for requesting RSS feeds only as often as needed, and
storing in a database the data about how often what feeds can be
requested.

This is a subclass of XML::RSS::TimingBot's methods that stores its data
in a DBI database object that you specify, instead of using
XML::RSS::TimingBot's behavior of storing in a local flat-file database.

To use this class, "use" it, create a new object of this class, and "use
DBI" and make a new database handle-object; then use "rssagent_dbh" to
assign that handle to this TimingBotDBI object; and use
"rssagent_url_field", "rssagent_lastmod_field",
"rssagent_nextupdate_field", and "rssagent_fetag_field" to set up the
right table/field names; and then, finally, you can use the TimingBotDBI
object just like a LWP::UserAgent (actually LWP::UserAgent::Determined)
object, to request RSS feeds.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/RSS/TimingBotDBI.pm
%{perl_vendorlib}/XML/RSS/*.pl

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.01-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.01-1
- Initial package.
