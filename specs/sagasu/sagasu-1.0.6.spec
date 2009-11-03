# $Id$

# Authority: dag

Summary: GNOME tool to find strings in multiple files
Name: sagasu
Version: 1.0.6
Release: 0%{?dist}
License: GPL
Group: Applications/Text
URL: http://sarrazip.com/dev/sagasu.html

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


#BuildRequires: gnomemm-devel >= 1.2

%description
GNOME tool to find words in multiple files.
The user specifies the search directory and the set of files
to be searched.  Double-clicking on a search result launches a
user command that can for example load the file in an editor
at the appropriate line.  The search can optionally ignore
CVS directories.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/sagasu/
%{_bindir}/*
%{_datadir}/sagasu/
%{_datadir}/gnome/apps/Utilities/*.desktop
%{_datadir}/pixmaps/*

%changelog
* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 1.0.6-0
- Initial package. (using DAR)
