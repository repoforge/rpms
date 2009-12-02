# $Id$
# Authority: shuff
# Upstream: Gordon Grubert <grubert$physik,uni-greifswald,de>

Summary: Create HTML summary of CUPS page accounting log
Name: cups-pagelog-analyzer
Version: 1.2
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://fachschaft.physik.uni-greifswald.de/~stitch/

Source: http://fachschaft.physik.uni-greifswald.de/~stitch/files_misc/cups-pagelog-analyzer-%{version}.tar.bz2
Patch0: %{name}_cssdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: sed
Requires: perl
Requires: perl(CGI)
Requires: perl(GD::Graph::pie)

Provides: pagelog_analyzer

%description
This program analyzes the page_log file of the CUPS printing system and creates
an HTML statistics output about the printer usage as well as the user's printed
pages.


%prep
%setup
%patch0 -p1

%build
# rename executable
mv pagelog_analyzer.pl pagelog_analyzer
# fix DATADIR
sed -i -e 's,DATADIR,%{_datadir}/%{name},' pagelog_analyzer

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir}
%{__install} -d %{buildroot}%{_datadir}/%{name}
%{__install} -m 0755 pagelog_analyzer %{buildroot}/%{_bindir}
%{__install} -m 0644 main.css %{buildroot}/%{_datadir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc readme.txt alias.conf
%{_bindir}/*
%{_datadir}/%{name}

%changelog
* Wed Dec 02 2009 Steve Huff <shuff@vecna.org> - 1.2-1
- Initial package.
