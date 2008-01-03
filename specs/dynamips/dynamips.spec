# $Id$
# Authority: dries

Summary: Cisco simulator
Name: dynamips
Version: 0.2.7
Release: 1
License: GPL
Group: Applications/Emulators
URL: http://www.ipflow.utc.fr/index.php/Cisco_7200_Simulator

Source: http://www.ipflow.utc.fr/dynamips/dynamips-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap-devel

%description
The goals of this emulator are mainly:
 * To be used as a training platform, with software used in real world. It 
   would allow people to become more familiar with Cisco devices, Cisco 
   being the world leader in networking technologies ;
 * Test and experiment the numerous and powerful features of Cisco IOS ;
 * Check quickly configurations to be deployed later on real routers.

Of course, this emulator cannot replace a real router: you should be able to 
get a performance of about 1 kpps (depending on your host machine), to be 
compared to the 100 kpps delivered by a NPE-100 (the oldest NPE model). So, 
it is simply a complementary tool to real labs for administrators of Cisco 
networks or people wanting to pass their CCNA/CCNP/CCIE exams.

%prep
%setup
%{__perl} -pi.orig -e 's|DESTDIR\)/man|DESTDIR)%{_mandir}|g; s|DESTDIR\)/bin|DESTDIR)%{_bindir}|g;' Makefile

%build
%{__make} %{?_smp_mflags} PCAP_LIB=-lpcap

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README* TODO
%doc %{_mandir}/man1/dynamips.1*
%doc %{_mandir}/man1/nvram_export.1*
%doc %{_mandir}/man7/hypervisor_mode.7*
%{_bindir}/dynamips
%{_bindir}/nvram_export

%changelog
* Thu Jan  3 2008 Dries Verachtert <dries@ulyssis.org> - 0.2.7-1
- Initial package.
