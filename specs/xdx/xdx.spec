# $Id$
# Authority: dries
# Upstream: Joop Stakenborg <pg4i$xs4all,nl>

Summary: Client to connect to a DX-cluster for amateur radio
Name: xdx
Version: 2.1
Release: 1
License: GPL
Group: Applications/Utilities
URL: http://www.qsl.net/pg4i/linux/xdx.html

Source: http://www.qsl.net/pg4i/download/xdx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: 
#Requires:

%description
Xdx is a client to connect to a DX-cluster for amateur radio. DX messages 
will be displayed in a list, and announcements will go to a text display. 
In addition to the usual functions, if you have hamlib installed it can 
control the radio and set the frequency simply by double clicking a DX-spot 
(using rigctl).

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/xdx*
%{_bindir}/xdx
%{_datadir}/xdx/
%{_datadir}/applications/Xdx.desktop

%changelog
* Sat May 27 2006 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Initial package.
