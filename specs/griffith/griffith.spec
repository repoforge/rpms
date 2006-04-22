# $Id$
# Authority: dries

Summary: Film collection manager application
Name: griffith
Version: 0.6.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://griffith.vasconunes.net/

Source: http://download.berlios.de/griffith/griffith-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: 
#Requires:

%description
Griffith is a film collection manager application. Adding items to the
movie collection is as quick and easy as typing the film title and
selecting a supported source. Griffith will then try to fetch all the
related information from the Web.  

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}
%{__rm} -f %{buildroot}%{_bindir}/griffith
%{__ln_s} %{_datadir}/griffith/lib/griffith %{buildroot}%{_bindir}/griffith
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%doc %{_mandir}/man1/griffith*
%doc %{_mandir}/man5/griffith*
%doc %{_mandir}/*/man1/griffith*
%doc %{_mandir}/*/man5/griffith*
%{_bindir}/griffith
%{_datadir}/griffith/
%{_datadir}/pixmaps/griffith.*
%{_datadir}/applications/griffith.desktop

%changelog
* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.1-1
- Initial package.
